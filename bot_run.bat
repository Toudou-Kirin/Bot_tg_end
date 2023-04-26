@echo off

call %~dp0Bot_tg\venv\Scripts\activate

cd %~dp0Bot_tg

set TOKEN=6185099015:AAEE4f_qNGAOz_PjfsC6i8RBCgUCtEtE3O8

python bot_telegram.py

pause