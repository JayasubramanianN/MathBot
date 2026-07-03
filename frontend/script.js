const API_URL = "http://127.0.0.1:8000/chat";

const chatBox = document.getElementById("chat-box");

async function sendMessage(){

    const input = document.getElementById("message");

    const message = input.value.trim();

    if(message==="") return;

    addMessage(message,"user");

    input.value="";

    try{

        const response = await fetch(API_URL,{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                message:message
            })

        });

        const data = await response.json();

        addMessage(data.answer,"bot");

    }

    catch(error){

        addMessage("Server Error","bot");

    }

}

function addMessage(text,type){

    const div=document.createElement("div");

    div.className=type+"-message";

    div.textContent=text;

    chatBox.appendChild(div);

    chatBox.scrollTop=chatBox.scrollHeight;

}

document.getElementById("message")
.addEventListener("keypress",function(e){

    if(e.key==="Enter"){

        sendMessage();

    }

});