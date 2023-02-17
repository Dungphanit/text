import cv2
import os

# Đường dẫn đến thư mục chứa ảnh
image_folder = "D:/python/anh"

# Danh sách tên các tập tin ảnh
images = [f for f in os.listdir(image_folder) if f.endswith(".jpg")]

for image in images:
    # Đọc tập tin ảnh
    img = cv2.imread(os.path.join(image_folder, image))

    # Hiển thị ảnh
    cv2.imshow(image, img)

    # Nếu bấm phím q, dừng việc đọc chuỗi ảnh
    if cv2.waitKey(0) & 0xFF == ord('a'):
        break

# Xóa cửa sổ hiển thị
cv2.destroyAllWindows()