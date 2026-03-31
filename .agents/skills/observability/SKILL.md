| name | observability |
| --- | --- |
| description | Query logs and traces from VictoriaLogs and VictoriaTraces to diagnose errors, investigate failures, and understand system behavior. Use when the user asks about errors, system health, or needs to debug issues. |
| argument-hint | [time_range, service_name, trace_id] |

Use the observability tools (logs_search, logs_error_count, traces_list, traces_get) to access structured logs and distributed traces from the backend.

## Steps

1. **Check for errors first**: When the user asks about system problems or errors, start by searching logs using `logs_search` or counting errors with `logs_error_count`.
   - Example queries:
     - `_stream:{service="backend"} AND level:error` — find all backend errors
     - Use `time_range` parameter to limit search to recent events (e.g., "1h", "30m")

2. **Analyze specific service logs**: If investigating a particular service, filter logs by service name:
   - `_stream:{service="<service_name>"} AND level:error`
   - Common services: `backend`, `postgres`, `nanobot`

3. **Find traces for detailed investigation**: If logs mention a trace ID or you need to see the full request flow:
   - Use `traces_list` to get recent traces for a service
   - Use `traces_get` with a specific trace ID to see the complete span hierarchy

4. **Correlate logs and traces**: When you find an error in logs, look for a trace ID in the log entry. Then fetch that trace to see which service/span failed.

5. **Summarize findings clearly**: Don't dump raw JSON. Instead, provide:
   - Error count and affected services
   - Time range of errors
   - Root cause if identifiable from logs/traces
   - Relevant trace IDs for further investigation

6. **Handle "no errors" case gracefully**: If no errors are found, confirm that the system is healthy and report the time range checked.

## Examples

**User asks**: "Any errors in the last hour?"

**Agent response**:
- Call `logs_error_count` with `service="backend"` and `time_range="1h"`
- If errors found: "Found 3 errors in the backend service in the last hour. The errors are related to database connection failures. Trace IDs: abc123, def456."
- If no errors: "No errors detected in the backend service in the last hour. System is healthy."

**User asks**: "What happened to request trace xyz789?"

**Agent response**:
- Call `traces_get` with `trace_id="xyz789"`
- Summarize the trace: "Request xyz789 started at service A, called service B, which failed with a 500 error at the database query step. Total duration: 1.2s."

## Important Notes

- Always use LogsQL syntax for VictoriaLogs queries. The basic format is: `_stream:{label="value"} AND field:value`
- VictoriaLogs and VictoriaTraces run inside Docker Compose, so they're accessible at internal hostnames (already configured in MCP tools)
- If a query fails, check the error message — it might be a syntax error in LogsQL
- Don't show raw JSON to users unless explicitly asked. Parse and summarize instead.
