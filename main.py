import os

JOKE = "Our AI agent merged its PR mid-demo, hit a merge conflict with itself, and fixed it by deleting my code; the demo crashed, but the conflict was gone."

if not 1 <= len(JOKE) <= 280:
    raise SystemExit("JOKE must be 1-280 characters")

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()