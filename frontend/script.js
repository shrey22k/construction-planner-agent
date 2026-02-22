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

  // format risk description into bullet list
  const riskElem = document.getElementById("risk");
  if (data.risk) {
    const parts = data.risk.split('•').map(p => p.trim()).filter(p=>p);
    riskElem.innerHTML = parts.length > 1
      ? '<ul>' + parts.map(p=>`<li>${p}</li>`).join('') + '</ul>'
      : data.risk;
  } else {
    riskElem.textContent = '';
  }

  const sev = document.getElementById("severity");
  sev.textContent = "Severity: " + data.severity;
  sev.className = "severity " + data.severity;

  document.getElementById("gantt").src =
    "http://127.0.0.1:5000/gantt.png?"+Date.now();

  // once results are in, stack risk and gantt vertically to accommodate long text
  const row = document.querySelector('.flex-row');
  if (row) row.classList.add('stacked');
}

function animateProgress() {
  let bar = document.getElementById("progressBar");
  bar.style.width = "10%";
  setTimeout(()=>bar.style.width="40%",400);
  setTimeout(()=>bar.style.width="70%",800);
}

function toggleTheme() {
  const btn = document.getElementById("themeBtn");
  const isDark = document.body.classList.toggle("dark");
  btn.textContent = isDark
    ? "🌗 Dark Mode: On"
    : "🌗 Dark Mode: Off";
}

// voice recognition function left for potential future use
function startVoice() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.start();
  recognition.onresult = e => {
    document.getElementById("goal").value = e.results[0][0].transcript;
  };
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

// make Enter key behave like clicking the "Generate Plan" button instead of reloading
document.getElementById("goal").addEventListener("keydown", event => {
  if (event.key === "Enter") {
    event.preventDefault();
    runPlanner();
  }
});
