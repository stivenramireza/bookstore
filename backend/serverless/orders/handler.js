// DB connection
const mongoose = require('mongoose');
const AutoIncrement = require('mongoose-sequence')(mongoose);

const connectDB = async() =>{
  const uri = `mongodb://${process.env.DOCUMENTDB_USERNAME}:${process.env.DOCUMENTDB_PASSWORD}@${process.env.DOCUMENTDB_HOSTNAME}:27017/?ssl=true&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false`
  try{
      const conn = await mongoose.connect(uri, {
          //useUnifiedTopology: true,
          useNewUrlParser: true,
          useCreateIndex: true,
          sslCA: require('fs').readFileSync(`${__dirname}/rds-combined-ca-bundle.pem`)
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
});

OrderSchema.plugin(AutoIncrement, { id:'order_seq', inc_field: 'order_id' });
Order = mongoose.model('Order', OrderSchema);

// Email service
const axios = require('axios');

const sendEmail = async(orderId) => {
  // TODO Send order email confirmation with JWT
  try {
    const url = `${process.env.EMAILS_API}/send`
    await axios.post(url, {
      item_id: orderId,
      email_type: 'order'
    })
    return 'Email has been sent successfully'
  } catch (err) {
    return `Error to send email: ${err}`
  }
}


// Serverless application
const serverless = require('serverless-http');
const express = require('express');

const cors = require('cors');
const helmet = require('helmet');
const bodyParser = require('body-parser');

const app = express();

app.use(cors());
app.use(helmet());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/order/status', (req, res, next) => {
  return res.status(200).json({message: 'Ok'})
});

app.get('/order/:id', async (req, res, next) => {
  try {
    const order = await Order.findOne({order_id: parseInt(req.params.id)}, '-_id -__v');
    return res.status(200).json(order);
  } catch (error) {
    return next(error);
  }
});

app.get('/orders', async (req, res, next) => {
  try {
    const orders = await Order.find({'customer.email': req.query.email}, '-_id -__v');
    return res.status(200).json(orders);
  } catch (error) {
    return next(error);
  }
});

app.post('/order', async (req, res, next) => {
  try {
    const createdOrder = await Order.create(req.body);
    await sendEmail(createdOrder.order_id)
    return res.status(201).json({message: 'Order has been created successfully and an email will be sent with all details'})
  } catch (error) {
    return next(error);
  }
});

module.exports.handler = serverless(app);
