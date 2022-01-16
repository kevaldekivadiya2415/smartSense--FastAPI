from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import DataframeInput
from bentoml.frameworks.sklearn import SklearnModelArtifact


@env(infer_pip_packages=True)
@artifacts([SklearnModelArtifact('model')])
class Classifier(BentoService):

    @api(input=DataframeInput(), batch=True)
    def predict(self, dataframe):
        dic = {0: "Salary not more then 50k", 1: "Salary more then 50k"}
        ans = int(self.artifacts.model.predict(dataframe))
        return dic[ans]