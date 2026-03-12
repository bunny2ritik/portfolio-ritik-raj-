import "./styles/Certifications.css";

const Certifications = () => {
  const researchPublications = [
    "Digital Resilience in Supply Chains",
    "Automating Software Defect Detection Through Machine Learning and LLMs",
    "Next-Generation Bioinformatics for Pulmonary Disease Research",
    "The Social Impact of Next-Generation Smart Cyber Technology",
    "Revolutionizing Sustainable Food Production With Quantum Computing",
  ];

  const patents = [
    {
      title: "Real-Time Method for Automated Street Parking Management",
      country: "India",
      status: "Published",
    },
    {
      title: "Intuitive Air Gesture Recognition System for Dynamic Computer Interaction Using Machine Learning",
      country: "Germany",
      status: "Registered",
    },
    {
      title: "IoT-Based Backup and Recovery System",
      country: "Germany",
      status: "Registered",
    },
    {
      title: "AI-Based Dark Web Threat Intelligence System",
      country: "Germany",
      status: "Registered",
    },
  ];

  const cybersecurityCerts = [
    "Google Cybersecurity Professional Certificate",
    "Ethical Hacking Essentials (EC-Council)",
    "Career Essentials in Cybersecurity – Microsoft & LinkedIn",
    "IBM Cybersecurity Analyst Assessment",
  ];

  const programmingCerts = [
    "Machine Learning with Python Developer Certification (~300 hours)",
    "Legacy JavaScript Algorithms & Data Structures – freeCodeCamp",
    "Responsive Web Design Developer Certification – freeCodeCamp",
    "Foundational C# with Microsoft Developer Certification",
  ];

  const skillCerts = [
    "Python (Basic) – HackerRank",
    "SQL (Basic / Intermediate / Advanced) – HackerRank",
    "C# (Basic) – HackerRank",
  ];

  const analyticsAndForensics = [
    { title: "Google Analytics Certification", category: "Data Analytics" },
    { title: "Advanced Google Analytics", category: "Data Analytics" },
    { title: "Data Analytics & Visualization Job Simulation – Forage", category: "Data Analytics" },
    { title: "Digital Forensics Course – OpenLearn (The Open University)", category: "Digital Forensics" },
  ];

  const networkingCerts = [
    "Understanding Networks",
    "Physical Network Infrastructure",
    "TCP/IP Protocols",
    "Network Security",
    "Advanced IP Networking",
    "Wireless & Cloud Networking",
  ];

  const achievements = [
    "Google Cloud Arcade – Cloud Milestone Achiever",
    "Multicloud World 2025 Conference Attendee",
    "Student Ambassador – Physics Wallah Campus Program",
    "Interaction with Oracle India Regional MD – Shailender Kumar",
  ];

  return (
    <section className="certifications-section" id="certifications">
      <div className="container-main">
        <h2 className="section-title">Certifications & Research</h2>

        <div className="certifications-grid">
          {/* Research Publications Card */}
          <div className="cert-card">
            <div className="cert-card-header">
              <span className="cert-card-icon">📚</span>
              <h3>Research Publications</h3>
            </div>
            <div className="cert-card-content">
              <p className="cert-card-subtitle">IGI Global Scientific Publishing</p>
              <ul className="research-list">
                {researchPublications.map((pub, idx) => (
                  <li key={idx} className="research-item">
                    <span className="research-bullet">→</span>
                    <span>{pub}</span>
                  </li>
                ))}
              </ul>
              <div className="cert-card-stats">
                <span className="stat-badge">{researchPublications.length} Publications</span>
              </div>
            </div>
          </div>

          {/* Patents Card */}
          <div className="cert-card patents-card">
            <div className="cert-card-header">
              <span className="cert-card-icon">⚡</span>
              <h3>Patents & Innovations</h3>
            </div>
            <div className="cert-card-content">
              <p className="cert-card-subtitle">Technology IP Portfolio</p>
              <div className="patents-list">
                {patents.map((patent, idx) => (
                  <div key={idx} className="patent-item">
                    <div className="patent-badges">
                      <span className="patent-badge">{patent.country}</span>
                      <span className="patent-status">{patent.status}</span>
                    </div>
                    <p className="patent-name">{patent.title}</p>
                  </div>
                ))}
              </div>
              <div className="cert-card-stats">
                <span className="stat-badge">{patents.length} Patents</span>
              </div>
            </div>
          </div>

          {/* Cybersecurity Certs Card */}
          <div className="cert-card">
            <div className="cert-card-header">
              <span className="cert-card-icon">🔐</span>
              <h3>Cybersecurity</h3>
            </div>
            <div className="cert-card-content">
              <p className="cert-card-subtitle">Professional Certifications</p>
              <div className="cert-tags">
                {cybersecurityCerts.map((cert, idx) => (
                  <span key={idx} className="cert-tag">
                    {cert}
                  </span>
                ))}
              </div>
              <div className="cert-card-stats">
                <span className="stat-badge">{cybersecurityCerts.length} Certs</span>
              </div>
            </div>
          </div>

          {/* Programming Certs Card */}
          <div className="cert-card">
            <div className="cert-card-header">
              <span className="cert-card-icon">💻</span>
              <h3>Programming & Development</h3>
            </div>
            <div className="cert-card-content">
              <p className="cert-card-subtitle">Advanced Certifications</p>
              <div className="cert-tags">
                {programmingCerts.map((cert, idx) => (
                  <span key={idx} className="cert-tag">
                    {cert}
                  </span>
                ))}
              </div>
              <div className="cert-card-stats">
                <span className="stat-badge">{programmingCerts.length} Certs</span>
              </div>
            </div>
          </div>

          {/* Skill Certifications Card */}
          <div className="cert-card">
            <div className="cert-card-header">
              <span className="cert-card-icon">🎯</span>
              <h3>Programming Skills</h3>
            </div>
            <div className="cert-card-content">
              <p className="cert-card-subtitle">Verified Proficiencies</p>
              <div className="cert-tags">
                {skillCerts.map((cert, idx) => (
                  <span key={idx} className="cert-tag">
                    {cert}
                  </span>
                ))}
              </div>
              <div className="cert-card-stats">
                <span className="stat-badge">{skillCerts.length} Certs</span>
              </div>
            </div>
          </div>

          {/* Data Analytics & Forensics Card */}
          <div className="cert-card">
            <div className="cert-card-header">
              <span className="cert-card-icon">📊</span>
              <h3>Analytics & Forensics</h3>
            </div>
            <div className="cert-card-content">
              <p className="cert-card-subtitle">Data & Security Analysis</p>
              <div className="cert-tags">
                {analyticsAndForensics.map((cert, idx) => (
                  <span key={idx} className="cert-tag" title={cert.category}>
                    {cert.title}
                  </span>
                ))}
              </div>
              <div className="cert-card-stats">
                <span className="stat-badge">{analyticsAndForensics.length} Certs</span>
              </div>
            </div>
          </div>

          {/* Networking Card */}
          <div className="cert-card">
            <div className="cert-card-header">
              <span className="cert-card-icon">🌐</span>
              <h3>Networking & Cloud</h3>
            </div>
            <div className="cert-card-content">
              <p className="cert-card-subtitle">CompTIA Network+ Knowledge</p>
              <div className="cert-tags">
                {networkingCerts.map((cert, idx) => (
                  <span key={idx} className="cert-tag">
                    {cert}
                  </span>
                ))}
              </div>
              <div className="cert-card-stats">
                <span className="stat-badge">{networkingCerts.length} Topics</span>
              </div>
            </div>
          </div>

          {/* Achievements Card */}
          <div className="cert-card achievements-card">
            <div className="cert-card-header">
              <span className="cert-card-icon">🏅</span>
              <h3>Achievements</h3>
            </div>
            <div className="cert-card-content">
              <p className="cert-card-subtitle">Professional Recognition</p>
              <ul className="achievements-list">
                {achievements.map((achievement, idx) => (
                  <li key={idx} className="achievement-item">
                    <span className="achievement-bullet">✓</span>
                    <span>{achievement}</span>
                  </li>
                ))}
              </ul>
              <div className="cert-card-stats">
                <span className="stat-badge">{achievements.length} Achievements</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Certifications;
