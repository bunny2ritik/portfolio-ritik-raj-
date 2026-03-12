import "./styles/Career.css";

const Career = () => {
  return (
    <div className="career-section section-container">
      <div className="career-container">
        <h2>
          My career <span>&</span>
          <br /> experience
        </h2>
        <div className="career-info">
          <div className="career-timeline">
            <div className="career-dot"></div>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Independent Cybersecurity Researcher</h4>
                <h5>Self-Directed Research & Practice</h5>
              </div>
              <h3>Jan 2020 – Present</h3>
            </div>
            <p>
              Actively involved in cybersecurity research, ethical hacking, and vulnerability analysis. Proficient with Metasploit, Burp Suite, Nmap, Wireshark, and SQLMap. Developed Python automation scripts for security testing, participated in CTF challenges and bug bounty programs, and studied exploit development and secure coding practices.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Android Application Developer</h4>
                <h5>Personal & Academic Projects</h5>
              </div>
              <h3>Ongoing</h3>
            </div>
            <p>
              Developed Android applications focusing on functionality and user experience. Built the Mait App, a college utility application with Room Database integration for Lost & Found system management. Implemented WebView services and designed custom navigation UI with animations.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Cybersecurity Intern / Security Expert</h4>
                <h5>Denitor Technologies – Ghaziabad</h5>
              </div>
              <h3>May 2024 – Aug 2024</h3>
            </div>
            <p>
              Worked with the cybersecurity team to identify vulnerabilities and strengthen system security. Performed Web Application Penetration Testing, SQL Injection analysis, and packet sniffing. Developed an advanced network scanner and contributed to improving system security through ethical hacking methodologies.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Cybersecurity Intern</h4>
                <h5>MIETY (Ministry of Electronics & Information Technology) – Government Institution</h5>
              </div>
              <h3>Sep 2025 – Feb 2026</h3>
            </div>
            <p>
              Interned at the Ministry of Electronics & Information Technology focusing on advanced cybersecurity research and national digital security initiatives. Engaged in vulnerability assessment, security architecture design, and development of security tools for government systems.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Career;
