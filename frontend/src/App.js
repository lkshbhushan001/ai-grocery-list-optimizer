import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import GroceryList from './components/GroceryList';
import ItemForm from './components/ItemForm';
import ShoppingCart from './components/ShoppingCart';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={GroceryList} />
        <Route path="/add-item" component={ItemForm} />
        <Route path="/cart" component={ShoppingCart} />
      </Switch>
    </Router>
  );
}

export default App;
