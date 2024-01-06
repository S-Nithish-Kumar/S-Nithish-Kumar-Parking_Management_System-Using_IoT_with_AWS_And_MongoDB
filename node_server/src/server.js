const express = require('express')
const path = require('path')
const bcrypt = require('bcrypt')
const {parkingStatusCollection, userCollection} = require('./config');

const app = express();

// convert data into json format
app.use(express.json())
app.use(express.urlencoded({ extended: false }));

app.set('view engine', 'ejs');

app.use(express.static("public"));

app.get("/", (req, res) => {
    res.render("login");
})

app.get("/signup", (req, res) => {
    res.render("signup");
})

app.get("/getData", async (req, res) => {
    const data = await parkingStatusCollection.find({status: 2});
    res.send(data)
})

app.get("/getUserName", async (req, res) => {
    const data = await userCollection.find({userId: req.query.userId});
    //console.log(data)
    res.send(data)    
})

app.get("/getUserSpace", async (req, res) => {
    const data = await parkingStatusCollection.find({userId: req.query.userId});
    //console.log(data)
    res.send(data)    
})

app.get("/getTotalAmount", async (req, res) => {
    const data = await parkingStatusCollection.find({userId: req.query.userId});
    //console.log(data)
    res.send(data)    
})

//Resister user
app.post("/signup", async (req, res) => {
    const data = {
        userId: req.body.userId,
        password: req.body.password,
        userName: req.body.userName,
        dataOfBirth: req.body.birthday,
        creditCardNumber: req.body.cardNumber,
        securityCode: req.body.securityCode
    }

    //check if the user name already exists in the database
    const existingUser = await userCollection.findOne({ userId: data.userId })
    if (existingUser) {
        res.send("User name already exists. Please choose a different username");
    }
    else {
        // hash the password using bcrypt
        const saltRounds = 10; // Number of salt round for bcrypt
        const hashedPassword = await bcrypt.hash(data.password, saltRounds);
        data.password = hashedPassword;

        const hashedCreditCardNumber = await bcrypt.hash(data.creditCardNumber, saltRounds);
        data.creditCardNumber = hashedCreditCardNumber;

        const securityCode = await bcrypt.hash(data.securityCode, saltRounds);
        data.securityCode = securityCode;

        const userData = await userCollection.insertMany(data);
        //console.log(userData);
        res.send("Successfully signed up. Please go back and login");
    }
});


// user login
app.post("/login", async (req, res) => {
    try {
        const check = await userCollection.findOne({ userId: req.body.userId });
        console.log(check);
        if (!check) {
            res.send("User name not found. Please SignUp");
        }
        else{
            // compare the hash password from the database with the plain text
            const isPasswordMatch = await bcrypt.compare(req.body.password, check.password);
            if (isPasswordMatch) {
                res.render("home",{query :check.userId});
            }
            else {
                res.send("Wrong password");
            }
        }
    }
    catch {
        res.send("Wrong Details");
    }
});

const port = 5000;
app.listen(port, () => {
    console.log(`Server running on Port: ${port}`);
});