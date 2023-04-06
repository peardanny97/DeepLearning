# LAB 03

## Problem 1

TensorflowCNN 클래스의 함수들이 주어진 설명에 맞게 동작하도록 코드를 작성하십시오.

```
class TensorflowCNN(tf.Module):
    def __init__(self, filter_list, learning_rate):
        '''
        filter_list를 저장해 놓고 __call__ 호출시 사용합니다.
        filter_list의 마지막 텐서의 out channel수가 class의 개수가 됩니다. 
        learning_rate는 fit에서 training시에 사용합니다.
        
        Inputs: 
        - filter_list: [filter_height, filter_width, in_channels, out_channels] 의 shape을 가진 텐서들의 리스트
        - learning_rate: float 값으로 optimizer의 learning rate로 설정해 줍니다.
        '''
        return
    
    def __call__(self, images):
        '''
        init에서 저장해 놓은 tensor들을 filter로 하여 convolution operation을 수행합니다.
        마지막에 1, 2 axis방향으로 reduce_mean을 수행하여 [batch_size, optdim]의 shape을 가지도록 하고 1 axis로 softmax를 수행합니다.
        convolution이외의 opearation은 사용하지 않습니다.
        
        Inputs: 
        - images: [batch_size, height, width, channel]의 shape을 가진 tensor입니다.
        
        Returns: 
        - result: convolution operation을 수행한 결과로 [batch_size, optdim]의 shape을 가진 tensor입니다.
        '''
        return result
    
    def fit(self, images, labels, epochs):
        '''
        images, labels을 이용하여 epochs 번 업데이트를 수행합니다.
        loss는 cross entropy를 이용하여 optimizer는 SGD를 이용합니다.
        learning_rate는 init에서 저장한 값을 이용합니다.
        
        Inputs: 
        - images: [batch_size, height, width, channel]의 shape을 가진 tensor입니다.
        - labels: [batch_size]의 shape을 가진 integer-valed tensor입니다. 0이상 클래스 수 미만의 값을 가집니다.
        - epochs: integer값으로 update step수를 나타냅니다.
        
        Returns: 
        - losses: float의 리스트로 
        '''
        return losses
    
    def save(self):
        '''
        saved_model이 아닌 checkpoint를 이용하여 저장합니다.
        '''
        return
    
    def restore(self):
        '''
        마지막 save함수가 호출 되었을 때의 값으로 variable의 값들을 set해 줍니다.
        '''
        return
```

## Problem 2

cifar100 dataset에 대해서 tensorflow를 이용하여 모델을 작성하고 training하여서 tf.saved_model.save(model, 'model')을 통해 저장하십시오.
- training이 완료된 model은 프로젝트 폴더 하위에 위치한 'model' 디렉토리에 저장되어 있어야 합니다.
- loaded_model = tf.saved_model.load('model')의 방법을 통해서 불러 올 수 있어야 하고 불러온 모델의 accuracy가 0.2 이상이면 정답으로 처리하겠습니다.

