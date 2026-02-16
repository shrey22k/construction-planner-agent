async function runPlanner() {

  const goal = document.getElementById("goal").value.trim();
  if (!goal) return alert("Enter goal");

  document.getElementById("thinking").style.display = "block";
  animateProgress();

  const res = await fetch("http://127.0.0.1:5000/plan", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({goal})
  });

  const data = await res.json();

  document.getElementById("thinking").style.display = "none";
  document.getElementById("progressBar").style.width = "100%";

  document.getElementById("goalOut").textContent = data.goal;

  document.getElementById("schedule").innerHTML =
    data.optimized_schedule.map((t,i)=>`<li>Step ${i+1}: ${t}</li>`).join("");

  document.getElementById("risk").textContent = data.risk;

  const sev = document.getElementById("severity");
  sev.textContent = "Severity: " + data.severity;
  sev.className = "severity " + data.severity;

  document.getElementById("gantt").src =
    "http://127.0.0.1:5000/gantt.png?"+Date.now();
}

function animateProgress() {
  let bar = document.getElementById("progressBar");
  bar.style.width = "10%";
  setTimeout(()=>bar.style.width="40%",400);
  setTimeout(()=>bar.style.width="70%",800);
}

function toggleTheme() {
  document.body.classList.toggle("light");
}

function exportPDF() {
  window.print();
}

function startVoice() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.start();
  recognition.onresult = e => {
    document.getElementById("goal").value = e.results[0][0].transcript;
  };
}
