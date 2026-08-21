@echo off
REM ============================================
REM  Open Week 9 Gemini Chatbot Project
REM  Double-click this file to launch Jupyter Notebook
REM ============================================

cd /d D:\AI\RAG

echo Starting Jupyter Notebook...
jupyter notebook

REM If "jupyter" isn't recognized, fall back to this method automatically
if errorlevel 1 (
    echo.
    echo "jupyter" command not found - trying alternate method...
    python -m notebook
)

pause
