import React, { useState} from "react";

import {
  FaBriefcase,
  FaBookmark,
  FaUsers,
  FaCheckCircle,
} from "react-icons/fa";
import "./CompanyDashboard.css"; 

const Dashboard = () => {
  const [stats /*setStats */] = useState([
    { title: "Posted jobs", count: 2, icon: FaBriefcase },
    { title: "Shortlisted", count: 3, icon: FaBookmark },
    { title: "Reviewed", count: 0, icon: FaCheckCircle },
    { title: "Applicants", count: 57, icon: FaUsers },
  ]);

  const [opportunities, /*setOpportunities */] = useState([
    { title: "Web Developer Volunteer at Coach Tribe (3 positions)", company: "Coach Tribe", posted: "2 weeks ago", category: "Back End Development", status: "Pending" },
    { title: "Front-end Developer Volunteer", company: "Dropify Technologies", posted: "3 weeks ago", category: "Product Development", status: "Pending" },
    { title: "Front-end Developer Volunteer", company: "Dropify Technologies", posted: "3 weeks ago", category: "Product Development", status: "Pending" }
  ]);

  return (
    <div className="Tdashboard">
      <h1>Dashboard</h1>
      <div className="stats">
        {stats.map((stat, index) => (
          <StatCard key={index} title={stat.title} count={stat.count} icon={stat.icon} />
        ))}
      </div>
      <div className="opportunities">
        <h3>Opportunities Applied Recently</h3>
        {opportunities.map((opportunity, index) => (
          <OpportunityCard key={index} opportunity={opportunity} />
        ))}
      </div>
    </div>
  );
};

const StatCard = ({ title, count, icon: Icon }) => {
  let color;
  let size;
  switch (title.toLowerCase()) {
    case "posted jobs":
      color = "#f17b54";
      size = "1.4rem";
      break;
    case "shortlisted":
      color = "#62f2c2";
      size = "1.5rem";
      break;
    case "reviewed":
      color = "#7079e5";
      size = "1.5rem";
      break;
    case "applicants":
      color = "#e7b214";
      size = "1.6rem";
      break;
    default:
      color = "#000";
      size = "1.5rem";
  }

  return (
    <div className={`stat ${title.toLowerCase()}-card`}>
      <div className="stat-info">
        <h2>{title}</h2>
        <div className="icon-and-count">
          <div className="icon-container">
            <Icon color={color} size={size} /> 
          </div>
          <p>{count}</p>
        </div>
      </div>
    </div>
  );
};


const OpportunityCard = ({ opportunity }) => (
  <div className="opportunity">
    <h4>{opportunity.title}</h4>
    <p>{opportunity.company} - Posted {opportunity.posted}</p>
    <p>Category: {opportunity.category}</p>
    <span className={`status ${opportunity.status.toLowerCase()}`}>{opportunity.status}</span>
  </div>
);

export default Dashboard;