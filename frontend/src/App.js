import React from 'react';
import GroceryList from './components/GroceryList';
import ItemForm from './components/ItemForm';

function App() {
    return (
        <div>
            <h1>AI Grocery Shopping List Optimizer</h1>
            <ItemForm />
            <GroceryList />
        </div>
    );
}

export default App;
