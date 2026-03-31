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

Here are the detailed scores for all labs:                                                                                                                                                                           

Lab 01 – Products, Architecture & Roles                                                                                                                                                                              

                                                                 
 Task                                        Avg Score  Attempts 
 ─────────────────────────────────────────────────────────────── 
 Lab setup                                   84.3%      3,436    
 Task 0: Practice the Git workflow           64.5%      306      
 Task 1: Product & architecture description  55.1%      161      
 Task 2: Roles and skills mapping            49.8%      83       
 Optional: Create a release                  60.0%      5        
 Optional: Resolve a merge conflict          34.6%      13       
 Optional: Add a CI check                    42.9%      7        
 Optional: Plan skill development            20.0%      5        
                                                                 

Lab 02 — Run, Fix, and Deploy a Backend Service                                                                                                                                                                      

                                                                     
 Task                                            Avg Score  Attempts 
 ─────────────────────────────────────────────────────────────────── 
 Task 1: Run the web server                      67.9%      210      
 Task 2: Identify, report, and fix a bug         66.7%      216      
 Task 4: Deploy the web server to the VM         56.2%      84       
 Optional 1: Implement the /outcomes endpoint    36.4%      11       
 Optional 3: Implement the post-order traversal  62.5%      6        
 Optional 2: Make your VM a proxy                0.0%       3        
                                                                     

Lab 03 — Backend API: Explore, Debug, Implement, Deploy                                                                                                                                                              

                                                                         
 Task                                                Avg Score  Attempts 
 ─────────────────────────────────────────────────────────────────────── 
 Task 1: Explore the API                             63.5%      382      
 Task 2: Enable and debug the interactions endpoint  66.4%      299      
 Task 4: Deploy to a hardened VM                     43.9%      110      
 Optional 2: Set up CI with GitHub Actions           44.0%      5        
 Task 3: Implement the learners endpoint             50.0%      4        
                                                                         

Lab 04 — Testing, Front-end, and AI Agents                                                                                                                                                                           

                                                                   
 Task                                          Avg Score  Attempts 
 ───────────────────────────────────────────────────────────────── 
 Task 1: Observe System Component Interaction  61.0%      688      
 Task 2: Back-end Testing                      59.8%      761      
 Task 3: Add Front-end                         56.3%      8        
 Optional 1: CI/CD with GitHub Actions         33.8%      17       
                                                                   

Lab 05 — Data Pipeline and Analytics Dashboard                                                                                                                                                                       

                                                      
 Task                             Avg Score  Attempts 
 ──────────────────────────────────────────────────── 
 Task 1: Build the Data Pipeline  73.5%      629      
 Task 2: Analytics Endpoints      64.4%      633      
 Optional 1: Grafana Dashboard    57.2%      60       
 Task 3: Dashboard Front-end      73.0%      23       
                                                      

Lab 06 — Build Your Own Agent                                                                                                                                                                                        

                                                      
 Task                             Avg Score  Attempts 
 ──────────────────────────────────────────────────── 
 Task 1: Call an LLM from Code    61.2%      682      
 Task 2: The Documentation Agent  74.0%      427      
 Task 3: The System Agent         42.8%      2,064    
                                                      

Lab 07 — Build a Client with an AI Coding Agent                                                                                                                                                                      

                                                                    
 Task                                           Avg Score  Attempts 
 ────────────────────────────────────────────────────────────────── 
 Task 1: Plan and Scaffold                      76.7%      768      
 Task 2: Backend Integration                    66.8%      570      
 Task 3: Intent-Based Natural Language Routing  58.8%      744      
 Task 4: Containerize and Document              66.6%      706      
                                                                    

Lab 08                                                                                                                                                                                                               

                                           
 Task                  Avg Score  Attempts 
 ───────────────────────────────────────── 
 (No tasks available)  —          —        
                                           

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Summary: Lab 02 has the lowest overall average score (~48.3%), largely due to "Optional 2: Make your VM a proxy" with 0.0%. Lab 07 has the highest overall average (~67.2%).

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

nanobot-1 | 🐈 Starting nanobot gateway version 0.1.4.post6 on port 18790...
nanobot-1 | MCP server 'lms': connected, 9 tools registered
nanobot-1 | Agent loop started

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

![description](plug.jpg)

## Task 3A — Structured logging

### Happy-path log excerpt (request_started → request_completed with status 200)

```
2026-03-31 12:07:41,529 INFO [app.main] [main.py:60] [trace_id=0bb1acc1e4e8309afc5040c8a0f5540d span_id=2be49e710c428281] - request_started
2026-03-31 12:07:41,530 INFO [app.auth] [auth.py:30] [trace_id=0bb1acc1e4e8309afc5040c8a0f5540d span_id=2be49e710c428281] - auth_success
2026-03-31 12:07:41,530 INFO [app.db.items] [items.py:16] [trace_id=0bb1acc1e4e8309afc5040c8a0f5540d span_id=2be49e710c428281] - db_query
2026-03-31 12:07:41,891 INFO [app.main] [main.py:68] [trace_id=0bb1acc1e4e8309afc5040c8a0f5540d span_id=2be49e710c428281] - request_completed
```

The structured logs show:
- `request_started` — the request entered the middleware
- `auth_success` — Bearer token authentication passed
- `db_query` — database query executed (select from `item` table)
- `request_completed` — response sent with HTTP 200

### Error-path log excerpt (db_query with error after stopping PostgreSQL)

After running `docker compose stop postgres` and triggering a request:

```
sqlalchemy.exc.InterfaceError: (sqlalchemy.dialects.postgresql.asyncpg.InterfaceError) <class 'asyncpg.exceptions._base.InterfaceError'>: connection is closed
[SQL: SELECT item.id, item.type, item.parent_id, item.title, item.description, item.attributes, item.created_at 
FROM item 
WHERE item.type = $1::VARCHAR]
```

The error shows the database connection was closed because PostgreSQL was stopped.

### VictoriaLogs query

![VictoriaLogs query result](3A.png)

Query: `_stream:{service.name="Learning Management Service"} AND severity:ERROR`

The VictoriaLogs UI at `http://localhost:42010/select/vmui` shows structured log entries with fields like `event`, `severity`, `trace_id`, `span_id`, and `service.name`.

## Task 3B — Traces

### Healthy trace

![Healthy trace](plug.jpg)

VictoriaTraces UI at `http://localhost:42011/select/vmui` shows traces for the Learning Management Service.

A healthy `GET /items/` request trace shows:
- **Trace ID**: e.g., `0bb1acc1e4e8309afc5040c8a0f5540d`
- **Service**: `Learning Management Service`
- **Spans**:
  - `request_started` — middleware entry
  - `auth_success` — authentication span
  - `db_query` — database operation (select from `item` table)
  - `request_completed` — response sent

All spans complete successfully with no errors.

### Error trace

![Error trace](plug.jpg)

After stopping PostgreSQL, the error trace shows:
- **Error**: `sqlalchemy.exc.InterfaceError: connection is closed`
- **Location**: `app.db.items` — database query failed
- **Root cause**: PostgreSQL connection refused

The trace hierarchy clearly shows where the failure occurred in the request flow.

## Task 3C — Observability MCP tools

### Agent response to "Any errors in the last hour?" (normal conditions)

The agent used the observability MCP tools (`logs_error_count`, `logs_search`, `traces_list`) to check for errors:

> **Good news on logs, but there's a system issue:**
>
> 📊 **Error Logs (last hour):** No error entries found in VictoriaLogs for the backend service or across all services.
>
> ⚠️ **System Health Issue:** The LMS backend health check shows the system is **unhealthy**:
> - Status: `unhealthy`
> - Error: `connection refused (http://localhost:42002)`
>
> This suggests the LMS backend service may be down or not responding on port 42002. The traces API also returned an error, which could be related to the same connectivity issue.
>
> Would you like me to investigate further or help troubleshoot the backend service?

### Tools registered in MCP server

- `logs_search` — search VictoriaLogs using LogsQL query syntax
- `logs_error_count` — count errors per service over a time window
- `traces_list` — list recent traces for a given service
- `traces_get` — fetch a specific trace by ID

### Observability skill

The skill prompt at `nanobot/workspace/skills/observability/SKILL.md` teaches the agent:
- When to use observability tools (errors, failures, incidents, diagnostics)
- How to search logs first, then check traces if trace IDs are found
- How to summarize findings concisely without dumping raw JSON

## Task 4A — Multi-step investigation

<!--
Add MCP observability tools testing evidence below:
1. Agent response to "Any errors in the last hour?" under normal conditions
2. Agent response to the same question after stopping PostgreSQL (showing real errors)
3. Include screenshots or console output showing the agent querying logs and traces
-->

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
