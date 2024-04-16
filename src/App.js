// App.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    async function fetchArticles() {
      try {
        const response = await axios.get('http://localhost:5000/list/articles');
        setArticles(response.data);
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    }
    fetchArticles();
  }, []);

  return (
    <div className="container">
      <header>
        <h1 className="title">Thể thao</h1>
      </header>
      <main>
        <ul className="articles-list">
          {articles.map(article => (
            <li className="article" key={article.id}>
              <div className="article-content">
                <h2 className="article-title">{article.title}</h2>
                <p className="article-description">{article.content}</p>
              </div>
              <div className="article-thumbnail">
                <img src={article.image} alt={article.title} />
              </div>
            </li>
          ))}
        </ul>
      </main>
      <footer>
        <p className="footer-text">© 2024 Vietnam News</p>
      </footer>
    </div>
  );
}

export default App;
