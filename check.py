import os

def check_project_structure():
    print("🔍 Checking Project Structure...")
    
    required_files = {
        "lib/models/artifact_model.dart": False,
        "lib/screens/artifact_detail_screen.dart": False,
        "lib/screens/scan_page.dart": False,
        "lib/main.dart": False
    }
    
    duplicates = []

    for root, dirs, files in os.walk("lib"):
        for file in files:
            full_path = os.path.join(root, file).replace("\\", "/")
            
            # Check if this is a known required file
            if full_path in required_files:
                required_files[full_path] = True
                print(f"✅ Found: {full_path}")
            
            # Check for duplicates in 'pages' folder (Common error)
            if "pages" in full_path and file in ["scan_page.dart", "artifact_detail_screen.dart"]:
                duplicates.append(full_path)
                print(f"❌ DUPLICATE FOUND: {full_path} (You should delete this!)")

    print("\n--- SUMMARY ---")
    missing = [f for f, found in required_files.items() if not found]
    
    if missing:
        print("🚨 MISSING FILES:")
        for f in missing:
            print(f"   - {f}")
    else:
        print("✅ All required files are present.")

    if duplicates:
        print("\n⚠️ CONFLICT WARNING:")
        print("You have duplicate files in 'lib/pages/'. The app might be importing the WRONG one.")
        print("Please delete the 'lib/pages' folder if you are using 'lib/screens'.")

if __name__ == "__main__":
    check_project_structure()