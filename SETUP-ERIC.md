# Setup Instructions (Eric)

## One-time setup: Install Python

1. Go to https://www.python.org/downloads/
2. Click the big yellow "Download Python" button
3. Run the installer — **check "Add Python to PATH"** during install
4. Restart your terminal after install

## Every time you work on the presentation

1. Open a terminal (Command Prompt or PowerShell)
2. Navigate to the project folder:
   ```
   cd path\to\Deako-Risewell
   ```
3. Pull latest changes:
   ```
   git pull
   ```
4. Start the server:
   ```
   python server.py
   ```
5. Open in your browser: **http://localhost:8080/presentation.html**

## Making text edits

1. Click the **pencil icon** (bottom-right, next to the chat icon)
2. "EDIT MODE" banner appears at top
3. Click any text to edit it directly
4. Press **Enter** or click away when done — changes auto-save
5. Click the pencil icon again to exit edit mode

Your edits are saved to `edits.json` in the project folder automatically. Claude will pick these up before making any code changes.

## Important

- Always use `http://localhost:8080/presentation.html` — NOT the `file://` URL
- If you open via `file://`, your edits won't save to the file
- Keep the terminal with `server.py` running while you work
- Press `Ctrl+C` in the terminal to stop the server when done
