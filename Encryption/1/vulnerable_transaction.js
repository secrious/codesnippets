/**
 * Vulnerable as code stores transaction in cleartext, including the credit card number!
 */
var transaction = {"custName":custName,"address":custAddress,"creditCardNumber":custCC.CCPAN};
s3.putObject({
    "Bucket": "ACME-customer-billing",
    "Key": "todayTransactions",
    "Body": JSON.stringify(transaction),
    "Content-Type": "application/json"
},
function(err,data){
});