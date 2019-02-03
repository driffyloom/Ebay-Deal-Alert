var webpack = require('webpack');
var minify = require('minify');

module.exports = {
  entry: {
    app: __dirname + '/static/src/js/app.jsx',
  },
  module: {
    rules: [
      { 
        test: [/\.jsx$/],
        exclude: /node_modules/,
        loader: 'babel-loader',

        query: {
          presets: ['@babel/preset-env', '@babel/preset-react']
        }
      },
      {
        test: require.resolve('jquery'),
        use: [{
            loader: 'expose-loader',
            options: 'jQuery'
        },{
            loader: 'expose-loader',
            options: '$'
        }]
      },
      {
        test: /\.css$/,
        loader: "style-loader!css-loader"
      },
      {
        test: /\.(ttf|eot|woff|woff2|otf)$/,
        use: {
          loader: "file-loader",
          options: {
            name: "fonts/[name].[ext]",
          },
        },
      },
      {
        test: /\.(gif|svg|jpg|png|pdf)$/,
        loader: "file-loader",
      },
    ],
  },
  output: {
    filename: '[name].js',
    path: __dirname + '/static/dist'
  }
};