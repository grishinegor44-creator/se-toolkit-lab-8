# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

The agentic loop is a framework describing how autonomous agents (like AI systems) interact with their environment through continuous cycles of perception, reasoning, planning, and action. Here's a breakdown:     

 1 Perception: The agent receives input from its environment (e.g., user queries, sensor data, or system events).                                                                                                    
 2 Reasoning: The agent processes this input to understand context, identify goals, and evaluate options.                                                                                                            
 3 Planning: The agent formulates a strategy or sequence of actions to achieve its goals.                                                                                                                            
 4 Action: The agent executes the plan, updating the environment (e.g., responding to a user, modifying a file).                                                                                                     

The loop then repeats, allowing the agent to learn from outcomes and refine future decisions. This enables adaptive, goal-oriented behavior in dynamic environments.                                                 

For example, when you ask "What is 2+2?", I perceive the query, reason through arithmetic, plan the response, and act by providing the answer.

The current workspace contains these directories/files but no LMS labs or lab-related content:                                                                                                                       

 • memory/                                                                                                                                                                                                           
 • sessions/                                                                                                                                                                                                         
 • skills/                                                                                                                                                                                                           
 • USER.md                                                                                                                                                                                                           
 • AGENTS.md                                                                                                                                                                                                         
 • HEARTBEAT.md                                                                                                                                                                                                      
 • SOUL.md                                                                                                                                                                                                           
 • TOOLS.md                                                                                                                                                                                                          

Would you like me to:                                                                                                                                                                                                

 1 Check if labs exist in a specific directory?                                                                                                                                                                      
 2 Search for lab-related files in the workspace?                                                                                                                                                                    
 3 Help you access the LMS directly? 

## Task 1B — Agent with LMS tools

<!-- Paste the agent's response to "What labs are available?" and "Describe the architecture of the LMS system" -->

1. The following labs are available in the LMS:
    Lab 01 – Products, Architecture & Roles
    Lab 02 — Run, Fix, and Deploy a Backend Service
    Lab 03 — Backend API: Explore, Debug, Implement, Deploy
    Lab 04 — Testing, Front-end, and AI Agents
    Lab 05 — Data Pipeline and Analytics Dashboard
    Lab 06 — Build Your Own Agent
    Lab 07 — Build a Client with an AI Coding Agent
    lab-08

2. Based on the pass rate data for all labs, here are the average scores per lab:                                                                                                                                       

                        
   Lab     Average Score  
   ────────────────────── 
   lab-01  51.4%          
   lab-02  48.3%          
   lab-03  53.6%          
   lab-04  52.7%          
   lab-05  67.0%          
   lab-06  59.3%          
   lab-07  67.2%          
   lab-08  N/A (no tasks)                     

   Lab 02 — Run, Fix, and Deploy a Backend Service has the lowest pass rate with an average score of approximately 48.3%.                                                                                               

   Notably, lab-02 includes a task "Optional 2: Make your VM a proxy" with a 0.0% average score, which significantly impacts the overall average. 


## Task 1C — Skill prompt

<!-- Paste the agent's response to "Show me the scores" (without specifying a lab) -->

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
