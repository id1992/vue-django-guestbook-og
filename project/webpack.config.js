var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker') 
var WriteFilePlugin = require('write-file-webpack-plugin')

module.exports = {
  // 시작점
  entry: './src/main.js',
  output: {
    // 컴파일된 파일 찾을 수 있는 곳
    path: path.resolve(__dirname, './static/dist'),
    // publicPath: '/dist/',
    filename: 'bundle.js'
  },
  plugins: [
    new BundleTracker({filename: 'webpack-stats.json'}),
    new WriteFilePlugin()
  ],
  module: {
    // 웹팩이 해당파일 만났을 때 사용할 툴
    rules: [
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ],
      },      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    overlay: true
  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}
