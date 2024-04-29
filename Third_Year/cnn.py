import torch
from torchvision import models
from torchvision.transforms import functional as F
import cv2

model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

image_path = r"Lambo.jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_tensor = F.to_tensor(image)
image_tensor = image_tensor.unsqueeze(0)

with torch.no_grad():
    output = model(image_tensor)
    
boxes = output[0]['boxes'].cpu().numpy()
scores = output[0]['scores'].cpu().numpy()
labels = output[0]['labels'].cpu().numpy()

for box, score, label in zip(boxes, scores, labels):
    if score > 0.5:
        cv2.rectangle(image, (int(box[0]), int(box[1])), (int(box[2])), (int(box[3])), (255, 0, 0), 2)
        cv2.putText(image, f'(label): {score}', (int(box[0]), int(box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0),2)
        
cv2.imshow("Object Detection", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()