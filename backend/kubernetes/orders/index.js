// Environment variables
const dotenv = require('dotenv');
dotenv.config();

// DB connection
const mongoose = require('mongoose');
const AutoIncrement = require('mongoose-sequence')(mongoose);

const connectDB = async() =>{
  const uri = process.env.DB_URI
  try{
      const conn = await mongoose.connect(uri, {
          useNewUrlParser: true,
          useCreateIndex: true
      })
      console.log(`DocumentDB is connected:${conn.connection.host}`.yellow)
  }catch(error){
      console.log(`Error to conect to DocumentDB: ${error.message}`.red.bold)
      process.exit(1)
  }
} 

connectDB()

// DB model
const OrderSchema = new mongoose.Schema({
  order_id: { type: Number }, 
  customer: {
    username: { type: String },
    email: { type: String }
  },
  items: { type: Array, default: [] },
  totalPrice: { type: Number }
}, { timestamps : true });

OrderSchema.plugin(AutoIncrement, { id:'order_seq', inc_field: 'order_id' });
Order = mongoose.model('Order', OrderSchema);

// Services
const axios = require('axios');

// Email service
const sendEmail = async(token, orderId) => {
  // TODO Send order email confirmation with JWT
  try {
    const url = `${process.env.EMAILS_API}/send`
    await axios.post(url, {
      item_id: orderId,
      email_type: 'order'
    }, {
      headers: {
        Authorization: token
      }
    })
    return 'Email has been sent successfully'
  } catch (err) {
    return `Error to send email: ${err}`
  }
}

// Auth service
const authenticated = async(req, res, next) => {
  try {
    const url = `${process.env.AUTH_API}/authenticate`;
    await axios.post(url, {}, {
      headers: {
        Authorization: req.get('Authorization')
      }
    });
    return next();
  } catch (error) {
    return res.status(401).json({message: 'Unauthorized'});
  }
}

// Microservice application
const express = require('express');

const cors = require('cors');
const helmet = require('helmet');
const bodyParser = require('body-parser');

const app = express();

app.use(cors());
app.use(helmet());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/order/status', (req, res) => {
  return res.status(200).json({message: 'Ok'})
});

app.get('/order/:id', authenticated, async (req, res, next) => {
  try {
    const order = await Order.findOne({order_id: parseInt(req.params.id)}, '-_id -__v');
    return res.status(200).json(order);
  } catch (error) {
    return next(error);
  }
});

app.get('/orders', authenticated, async (req, res, next) => {
  try {
    const orders = await Order.find({'customer.email': req.query.email}, '-_id -__v');
    return res.status(200).json(orders);
  } catch (error) {
    return next(error);
  }
});

app.post('/order', authenticated, async (req, res, next) => {
  try {
    const createdOrder = await Order.create(req.body);
    await sendEmail(req.get('Authorization'), createdOrder.order_id)
    return res.status(201).json({message: 'Order has been created successfully and an email will be sent with all details'})
  } catch (error) {
    return next(error);
  }
});

app.listen(process.env.PORT, () => {
  console.log(`Orders service is running at port ${process.env.PORT}`)
});
