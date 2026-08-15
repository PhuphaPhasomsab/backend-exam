## Question
![](/assets/q_idempotency.png)
## Response Section
Idempotency คือ การ ทำรายการ (request) เดิมมาซ้ำหลายครั้งโดยต้องทำให้ request นั้นต้องเกิดขึ้นแค่ครั้งเดียวไม่ว่าส่งมากี่ครั้งก็ตาม เช่นการโอนเงินต้องการโอนเงินแค่ครั้งเดียวแต่ดันมี 2 request ควรจะมีการทำ request ได้แค่ครั้งเดียว ถ้ามีเพื่มให้ reject 
โดยสามารถทำโดยการที่มี ID ของแต่ละ request ส่งไปด้วยโดย ให้ เช็คว่า ID นี้เคยทำรายการไปแล้วไหมถ้าทำแล้ว reject ถ้ายังก็ accept 

@app.route("/payments",methods=["post"])
def payment():
    id_key = request.headers.get("id_key")
    <!-- ไม่มี key ส่งมาด้วย -->
    if not id_key:
        return jsonify({
            "error":"id_key missing"
        }),400
        <!-- เจอ key ใน payments กันทำซ้ำ-->
    if id_key in payments:
        return jsonify({
            "message": "Payment already exists",
            "data": payments[id_key]
        }), 200
    data = request.get_json()
    amount = data.get("amount")
    payment = {
        "payment_id": len(payments) + 1,
        "amount": amount,
        "status": "success"
    }
    payments[id_key] = payment
    return jsonify(payment), 201