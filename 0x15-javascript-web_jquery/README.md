<img src="https://i.redd.it/7285bvqz43s01.png">

## JavaScript - Web jQuery

#### What is JavaScript?
JavaScript is a high-level, dynamic, and interpreted programming language used for creating interactive websites and web applications. It is a client-side scripting language, which means it is executed on the client-side (in the user's web browser) rather than on the server-side.

JavaScript is used to add dynamic and interactive behavior to HTML documents. It is commonly used for form validation, creating animations, and modifying the content of a web page based on user interactions.


### What is jQuery?
jQuery is a fast, small, and feature-rich JavaScript library. It simplifies HTML document traversal and manipulation, event handling, animation, and Ajax interactions for rapid web development.

With jQuery, you can easily manipulate the HTML and CSS of a web page, create animations, and handle events. It also provides an easy-to-use interface for making Ajax requests to a web server, allowing you to load and manipulate data without refreshing the entire page.

#### How to use jQuery?
To use jQuery in your web application, you need to include the jQuery library in your HTML document. You can either download the library and host it on your web server, or include it from a CDN (Content Delivery Network).

Here is an example of how to include jQuery from a CDN:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Web Page</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <!-- Your web page content here -->
</body>
</html>
```

Once you have included the jQuery library, you can use its functions to manipulate the HTML and CSS of your web page. Here is an example of how to change the text of a paragraph element using jQuery:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Web Page</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <p id="my-paragraph">Hello, World!</p>

  <script>
    $(document).ready(function() {
      $('#my-paragraph').text('Hello, jQuery!');
    });
  </script>
</body>
</html>
```

In this example, the $(document).ready() function is used to wait until the document is fully loaded before executing the jQuery code. The $('#my-paragraph') selector is used to select the paragraph element with the my-paragraph ID, and the text() function is used to change its text to "Hello, jQuery!".

#### Conclusion
JavaScript and jQuery are powerful tools for creating dynamic and interactive web applications. With their ease of use and wide range of features, they are essential tools for any web developer. By mastering JavaScript and jQuery, you can create amazing user experiences and take your web development skills to the next level.
