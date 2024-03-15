// GET http://127.0.0.1:105/search?start=avevi

pm.sendRequest("https://postman-echo.com/get", function (err, response) {
    console.log(response.json());
});


pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});


pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});


pm.test("Correct wpname and query", function () {
    pm.expect(pm.response.json().wpname).to.eql("avevi");
});
