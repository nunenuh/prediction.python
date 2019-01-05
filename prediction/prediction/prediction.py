from tsp.utils import Loader

class Prediction(object):
    def __init__(self, path):
        # self.model = Loader.load_model(path)
        pass

    def predict(self, **kwargs):
        raise NotImplementedError()

class TitanicPrediction(Prediction):

    def __init__(self, path):
        super(TitanicPrediction, self).__init__(path)

    def predict(self, **kwargs):
        print(kwargs['age'])
        if kwargs['sex'] == 'male':
            sex=0
        elif kwargs['sex'] == 'female':
            sex=1
        else:
            raise NameError("Use male or female")

if __name__ == '__main__':
    tp = TitanicPrediction('file.pth')
    tp.predict(age=25, sex='males', cabin=1)

