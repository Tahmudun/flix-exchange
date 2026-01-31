# Architecture

Flix Exchange ingests Instagram Messages export JSON (ZIP-unpacked), normalizes messages and reactions into SQLite, then serves analytics via an API consumed by a live dashboard.

Pipeline:
1) Import export folder
2) Parse + normalize messages/reactions
3) Store in SQLite
4) Compute metrics (leaderboard, inactivity)
5) Serve results to frontend
