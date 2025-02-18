from flask import Flask, render_template
from flask import request
import es_operation

app = Flask(__name__)

# set Elasticserch server
#ELASTIC_SERVER = 'localhost:9200'
ELASTIC_SERVER = '192.168.1.3:9200'
ELASTIC_SERVER = 'elasticsearch:9200'
es = es_operation.Ela(es_server=ELASTIC_SERVER)


# get category from Elasticsearch
index_name = 'test_image'
cates= es.get_category(index_name)


@app.route('/')
def index():
  return render_template("index.html", title="FF14_image", cates=cates)

@app.route('/pic', methods=['GET', 'POST'])
def post():
  #cate = request.form.get('cate')
  cate = request.args.get('cate')
  images = es.get_doc(index_name, cate) 
  return render_template('index.html', \
    title = 'FF14_image', \
    message = '{}'.format(cate), cates=cates, selected=cate, images=images)


if __name__ == '__main__':
  #app.debug = True
  app.run(host='0.0.0.0')
