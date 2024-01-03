const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  publicPath: '/',
  pages: {
    index: {
      // entry for the page
      entry: 'src/index/main.js',
      // the source template
      template: 'public/index.html',
      // output as dist/index.html
      filename: 'index.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Mapping Fossil Ties Database'
    },
    about: {
      // entry for the page
      entry: 'src/About/main.js',
      // the source template
      template: 'public/About.html',
      // output as dist/index.html
      filename: 'About.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'The Coalition'
    },
    FAQ: {
      // entry for the page
      entry: 'src/FAQ/main.js',
      // the source template
      template: 'public/FAQ.html',
      // output as dist/index.html
      filename: 'FAQ.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'FAQs'
    },
    Database: {
      // entry for the page
      entry: 'src/Database/main.js',
      // the source template
      template: 'public/Database.html',
      // output as dist/index.html
      filename: 'Database.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Mapping Fossil Ties Database'
    },
    News: {
      // entry for the page
      entry: 'src/News/main.js',
      // the source template
      template: 'public/News.html',
      // output as dist/index.html
      filename: 'News.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'In the news: Fossil Ties'
    }
  }
})
