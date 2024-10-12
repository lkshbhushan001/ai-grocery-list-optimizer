import React, { useState } from 'react';
import UserPreferences from './UserPreferences';
import GroceryList from './GroceryList';
import axios from 'axios';

const App = () => {
    const [groceryList, setGroceryList] = useState([]);
    const [userName, setUserName] = useState('');

    const fetchGroceryList = async () => {
        try {
            const response = await axios.post('http://localhost:5000/grocery-list', { name: userName });
            setGroceryList(response.data.grocery_list);
        } catch (error) {
            console.error('Error fetching grocery list', error);
        }
    };

    return (
        <div className="App">
            <h1>AI-Based Grocery Shopping List Optimizer</h1>
            <UserPreferences setUserName={setUserName} fetchGroceryList={fetchGroceryList} />
            <GroceryList items={groceryList} />
        </div>
    );
};

export default App;
