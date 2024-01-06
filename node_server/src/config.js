const mongoose = require("mongoose");
//const connect = mongoose.connect("mongodb://0.0.0.0:27017/userInfo")

const connectionURL = "mongodb+srv://Nithish007:2000@mycluster.dkov5yi.mongodb.net/vehicleDB?retryWrites=true&w=majority"

const connect = mongoose.connect(connectionURL)

//check database connected or not
connect.then(() => {
    console.log("Database connected successfully");
})
.catch(() => {
    console.log("Database cannot be connected");
});


// Create a schema
const loginSchema = new mongoose.Schema({
    userId: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    },
    userName: {
        type: String,
        required: true
    },
    dataOfBirth: {
        type: Date,
        required: true
    },
    creditCardNumber: {
        type: String,
        required: true
    },
    securityCode: {
        type: String,
        required: true
    }
});

const parkingStatusSchema = new mongoose.Schema({
    userId: {
        type: String,
        required: true
    },
    status: {
        type: Number,
        required: true
    },
    parkingSpaceNumber: {
        type: Number,
        required: true
    },
    entryTime: {
        type: Number,
        required: false
    },
    exitTime: {
        type: Number,
        required: false
    },
    totalAmount: {
        type: Number,
        required: false
    }
});


// collection
// const Model = mongoose.model("Model", fileSchema, "NameOfCollection");
const userCollection = new mongoose.model("users", loginSchema);
const parkingStatusCollection = new mongoose.model("vehicleStatus", parkingStatusSchema, "vehicleStatus");

module.exports = {parkingStatusCollection,userCollection};


// 