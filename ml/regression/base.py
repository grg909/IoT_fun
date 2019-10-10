from ml.base import BaseModel


class Regression(BaseModel):

    def __init__(self):
        BaseModel.__init__(self)
        self._features = None
        self._target = None

    # train the model with given data set
    def train(self, data):
        self._features = data["train"]
        self._target = data["target"]
        self._model.fit(self._features, self._target)

    # train the model with given data set
    def getParameterDef(self):
        pass

    def setParameter(self, parameter):
        pass

    # predict the model with given dataset
    def predict(self, data):
        return self._model.predict(data)

    def predictViz(self, scale):
        # Predict Viz only available for one dimensional dataset
        if len(self._features[0]) != 1:
            return None

        result = dict()
        result["predict"] = list()
        result["data"] = list()

        for i in range(0, len(self._features)):
            item = dict()
            item["x"] = self._features[i][0]
            item["y"] = self._target[i]
            result["data"].append(item)

        range_d = dict()
        range_d["xmin"] = self._features[0][0]
        range_d["xmax"] = self._features[0][0]

        for item in self._features:
            if item[0] > range_d["xmax"]:
                range_d["xmax"] = item[0]
            if item[0] < range_d["xmin"]:
                range_d["xmin"] = item[0]

        xstep = (float(range_d["xmax"]) - float(range_d["xmin"])) / scale

        for x in range(0, scale):
            dx = range_d["xmin"] + x * xstep

            onePredict = self.predict([[dx]])
            record = dict()
            record["x"] = dx
            record["y"] = onePredict[0]
            result["predict"].append(record)

        return result
