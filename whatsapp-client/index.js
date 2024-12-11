const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

// Create a new client instance
const client = new Client({
    authStrategy: new LocalAuth()
});


// When the client is ready, run this code (only once)
client.once('ready', () => {
    console.log('Client is ready!');
});

// When does not linked with client QR-Code
// client.on('qr', (qr) => {
//     qrcode.generate(qr, {small: true});
// });

client.on('message', message => {
    const payload = JSON.stringify({ question: message.body})
    console.log('Mensagem enviada!', payload)

    fetch('http://127.0.0.1:5000/chat/', { 
        method: "POST",
        body: payload,
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((res) => {
        console.log("Tratando resposta =>", res)
        return res.json()
    })
      .then(data => {
        console.log('Resposta ==>', data)
        client.sendMessage(message.from, data.answer)
      })
});

// Start your client
client.initialize();