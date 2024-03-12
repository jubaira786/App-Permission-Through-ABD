import subprocess

# Function to run ADB commands and capture the output
def run_adb_command(command):
    try:
        result = subprocess.run(
            ['adb', 'shell', command],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing ADB command: {e}")
        return None

# Function to list installed apps and their permissions
def list_installed_apps_with_permissions():
    # Get a list of installed apps
    installed_apps = run_adb_command('pm list packages -f')

    if installed_apps:
        app_list = installed_apps.split('\n')

        # Create a report file
        with open('app_permissions_report.txt', 'w') as report_file:
            for app in app_list:
                package_name = app.split('=')[1]
                permissions = run_adb_command(f'dumpsys package {package_name} | grep permission')

                if permissions:
                    report_file.write(f"App: {package_name}\n")
                    report_file.write("Permissions:\n")
                    report_file.write(permissions + "\n\n")

if __name__ == "__main__":
    list_installed_apps_with_permissions()
    print("App list saved to 'installed_apps_list.txt'")
    print("Permissions report saved to 'app_permissions_report.txt'")
