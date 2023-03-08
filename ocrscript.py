from ocr import ocr_space_file
import json

if __name__ == "__main__":
    dir = "./35/35_《南科新知》第九期.jpg"
    res = ocr_space_file(dir)
    with open("./res.json", "w", encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False)
        json_str = json.dumps(res, ensure_ascii=False)
        print(json_str)