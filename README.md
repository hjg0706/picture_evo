# 유전 알고리즘을 이용해 그림을 그려보자!

[사용법]
터미널에서 picture_evo과 기타 사항 입력하면 변환이 된다.
[예시 사용법]

	Picture "Junyeong 64.jpg" --size 1 --genes 256 --max-generations 50000

--size: 이미지 크기 {1: (64x64), 2: (128x128), 3: (256x256)} //기본값: 2
--genes: 원의 개수 // 기본값: 256
--max-generations: Number of generations to run // 기본값: 500,000

파이썬에서 사용 방법
(예시 스크립트)
```python
from picture_evo import evolution
from picture_evo import helpers
import numpy as np
import cv2

#타겟 로딩 (사이즈:64x64라 입력)
tar = helpers.load_target_image("XX.jpg", size=(64, 64))

e = evolution.Evolution((64, 64), tar)
#50000번 진화
e.evolve(max_generation=50000)
#진화된 표현형(사진)
helpers.show_image(e.specie.phenotype)
#유전형 저장
np.savetxt("Checkpoint.txt", e.specie.genotype)
#표현형 저장
cv2.imwrite("ImageOutput.jpg", e.specie.phenotype)
```

체크포인트 저장 방법 

```python
from circle_evolution import evolution
from circle_evolution import helpers
import numpy as np
import cv2

target = helpers.load_target_image("Mona Lisa 64.jpg", size=(64, 64))

e = evolution.Evolution((64, 64), target)

# 저장된 지점으로부터 로드
genes = np.loadtxt("Checkpoint.txt")
e.specie.genotype = genes

# 50k만큼 다시 진화
e.evolve(max_generation=50000)
```