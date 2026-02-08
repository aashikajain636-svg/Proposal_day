from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body{
    margin:0;
    height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    font-family:'Segoe UI',sans-serif;
    background: radial-gradient(circle at top, #ffe6ec, #fff);
}

.card{
    width:320px;
    padding:30px;
    background:white;
    border-radius:20px;
    box-shadow:0 15px 30px rgba(0,0,0,0.2);
    text-align:center;
}

button{
    margin:10px;
    padding:12px 22px;
    border:none;
    border-radius:30px;
    font-size:16px;
    cursor:pointer;
    background:#ff4d6d;
    color:white;
    transition:0.3s;
}

button:hover{
    background:#e6004c;
    transform:scale(1.05);
}

.hearts-row{
    display:flex;
    justify-content:center;
    gap:20px;
    margin-top:20px;
}

.heart-wrap{
    position:relative;
    font-size:60px;
}

.word{
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    font-size:14px;
    font-weight:bold;
    color:white;
}

textarea{
    width:100%;
    height:80px;
    border-radius:10px;
    padding:10px;
}
</style>
</head>
<body>

<div id="app"></div>

<script>
const app = document.getElementById("app");

/* STEP 1 */
function cardOne(){
    app.innerHTML = `
    <div class="card">
        <h2>💌 I have something special for you</h2>
        <button onclick="cardTwo()">Continue</button>
    </div>`;
}

/* STEP 2 */
function cardTwo(){
    app.innerHTML = `
    <div class="card">
        <h2>❓ Do you like me?</h2>
        <button onclick="yesCard()">Yes ❤️</button>
        <button onclick="noCard()">No 😅</button>
    </div>`;
}

/* YES FLOW */
function yesCard(){
    app.innerHTML = `
    <div class="card">
        <h4>I want to tell you something...</h4>

        <div class="hearts-row">
            <div class="heart-wrap">❤️<div class="word" id="w1"></div></div>
            <div class="heart-wrap">❤️<div class="word" id="w2"></div></div>
            <div class="heart-wrap">❤️<div class="word" id="w3"></div></div>
        </div>

        <button onclick="proposal()">Message for you 💌</button>
    </div>`;

    setTimeout(()=>{document.getElementById("w1").innerText="I";},600);
    setTimeout(()=>{document.getElementById("w2").innerText="Love";},1400);
    setTimeout(()=>{document.getElementById("w3").innerText="You";},2200);
}

function proposal(){
    app.innerHTML = `
    <div class="card">
        <h3>🌹 Happy Proposal Day🌹</h3>
        <p>
        I never planned to fall for someone like this… but then you came into my life and slowly became the most special part of it.
        With you, even silence feels beautiful and every moment feels worth remembering.
        <br><br>
        Will you be mine, today, tomorrow, and forever? ❤️
        </p>

        <button onclick="replyBox()">Waiting for your Reply 💌</button>
    </div>`;
}

/* NO FLOW */
function noCard(){
    app.innerHTML = `
    <div class="card">
        <h2>😌 I know you do like me…</h2>
        <p>Please say yes 🥺</p>
        <button onclick="cardTwo()">Go back</button>
    </div>`;
}

/* WHATSAPP REPLY */
function replyBox(){
    app.innerHTML = `
    <div class="card">
        <h3>Write your reply 💬</h3>
        <textarea id="msg" placeholder="Type your message..."></textarea>
        <br><br>
        <button onclick="sendWhatsApp()">Send via WhatsApp</button>
    </div>`;
}

function sendWhatsApp(){
    let message = document.getElementById("msg").value;
    let phone = "919205642068";   // ← PUT YOUR WHATSAPP NUMBER
    let url = "https://wa.me/" + phone + "?text=" + encodeURIComponent(message);
    window.open(url, "_blank");
}

cardOne();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10001)
