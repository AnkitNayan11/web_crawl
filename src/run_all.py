import subprocess

scripts = [
    "/Users/ankitnayan/Downloads/final_web_v1/web_crawl/src/programatic_login.py",
    "/Users/ankitnayan/Downloads/final_web_v1/web_crawl/src/main.py"
]

for script in scripts:
    print(f"\nRunning: {script}")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    
    # Print output and errors
    print(result.stdout)
    if result.stderr:
        print(f"Error in {script}:\n{result.stderr}")
