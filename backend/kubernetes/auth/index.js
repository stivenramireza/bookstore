// Environment variables
const dotenv = require('dotenv');
dotenv.config();

// Microservice application
const cors = require('cors');
const helmet = require('helmet');
const bodyParser = require('body-parser');

const express = require('express');
const app = express();

app.use(cors());
app.use(helmet());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Cognito middleware
const { CognitoJwtVerifier } = require('aws-cognito-jwt-verifier');
const verify = new CognitoJwtVerifier();

const authenticated = async(req, res) => {
  const token = req.get('Authorization');
  if (!token) return res.status(401).json({message: 'Unauthorized'});
  const verifiedToken = await verify.checkJwt(token.split(' ')[1], process.env.AWS_REGION, process.env.AWS_COGNITO_USER_POOL_ID);
  const status = JSON.parse(verifiedToken).status;
  if (!status) return res.status(401).json({message: 'Token is invalid or has expired'});
  return res.status(200).json({message: 'Authorized'});
}

app.get('/auth/status', (req, res) => {
  return res.status(200).json({message: 'Ok'});
});

app.post('/auth/authenticate', authenticated, (req, res, next) => {
  try {
    return res.status(200).json({message: 'Token has been validated successfully'});
  } catch (err) { 
    return next(err);
  }
});

app.listen(process.env.PORT, () => {
  console.log(`Auth service is running at port ${process.env.PORT}`)
});
