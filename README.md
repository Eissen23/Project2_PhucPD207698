# Project2_PhucPD207698 Setup Django - React project

### 1. Đi tới thư mục muốn sử dụng 
Sử dụng câu lệnh tạo môi trường ảo
		```py -m venv <tên mt ảo>```
Với các dependencies như sau:
Nó sẽ tạo ra mội thư mục chứa môi trường ào 
### 2. Kích hoạt môi trường ảo
- ==lưu ý== : đới với người dùng Window 11 thì cần phải set up thêm bước này
	- Khởi chạy terminal mặc định (powershell) sử dụng oftion "Run as administrator"
	- Chèn câu lệnh ```Set-ExecutionPolicy RemoteSigned```
Sau đó chạy file .ps1 để kích hoạt
		```<tên máy ảo>\Scripts\Activate.ps1```
### 3. Cài Django vào môi trường ảo
  ```py -m pip install Django```
### 4. Cài interpreter cho python project


# Cho React
### 1. Tạo app riêng cho react để đảm nhận sau đó di chuyển vào app
### 2. Tạo các folder 
	src
		components
	static
		frontend
		css
		images
	tempates
### 3. Viết ```npm init -y```
### 4. sử dụng npm install tải các package sau cùng flag
- webpack webpack-cli --save-dev
- @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
- react react-dom --save-dev
- npm install @material-ui/core --force
- @babel/plugin-proposal-class-properties --force
- npm install react-router-dom --legacy-peer-deps
- npm install @material-ui/icons --legacy-peer-deps
### 5. Babel.config.json
Trong frontend app tạo thư mục trên
Copy code này vào

````babel.config.json
{
  "presets": [
    [
      "@babel/preset-env",
      {
        "targets": {
          "node": "10"
        }
      }
    ],
    "@babel/preset-react"
  ],
  "plugins": ["@babel/plugin-proposal-class-properties"]
}
````

### 6. webpack.config.js
Trong folder frontend
```webpack
const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "./static/frontend"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],
};
```

### 7. Trong package.json 
```package
"scripts":{
	"dev": "webpack --mode development --watch",
	"build": "webpach --mode production"
}
```

# React integration

# Routing system
Trong file js của homepage sử dụng thư viện react-router-dom
```
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom"
```
Ở phần  render>return statement:
```
return (
	<Router>
		<Switch>
			<Route exact path='/' ><p>Blah blah homepage</p></Route>
			<Route path='/another' component= {AnotherComponent}><p>Blah blah another</p></Route>
		</Switch>
	</Router>
)
```
__Lưu ý__: 
	- sau mỗi lần thêm path vào React thì sẽ cần phải thêm path vào Django tương ứng
	- Route của react sẽ đọc các Route component từ trên xuống theo path và cần phải cẩn thận ở đó. Vì router của react chỉ chọn routing cái nó đọc đc đầu tiên: giả sử không có exact trong code trên, nếu ta theo đường dẫn '/another' thì cho dù xâu khác hoàn toàn, react vẫ sẽ render component có path = '/' vì 'another' cũng có 1 đoạn như vậy nên nó sẽ render nó. Vì thế cần phải lưu tâm và sử dụng exact nếu cần.

Ở urls.py ta thêm các đường urls vào 

#### Update:
Phần code trên chỉ có đước sử dụng cho React v5 trở về trc  nhưng giờ cần phải convert sang V6
[reactjs - Attempted import error: 'Switch' is not exported from 'react-router-dom' - Stack Overflow](https://stackoverflow.com/questions/63124161/attempted-import-error-switch-is-not-exported-from-react-router-dom)

# USED API 
  Hust logo [hust-logo-official_.3m.jpeg (787×1184) (storage.googleapis.com)](https://storage.googleapis.com/hust-files/5807675312963584/images/hust-logo-official_.3m.jpeg)


  project.urls.py
    app.urls.py
