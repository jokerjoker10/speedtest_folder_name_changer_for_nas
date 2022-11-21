# Speedtest folder name changer for nas

Deploy:

Install Python on your system.

Install the required library on your system:

```
python -m pip install speedtest-cli
```

Create a directory inside your base directory called: “speed_test_display”

Move the “data.csv” to the just created folder.

Add the base directory to the BASE_DIR var inside the .env file.

Add the main.py to your cron job list with the interval you want.
