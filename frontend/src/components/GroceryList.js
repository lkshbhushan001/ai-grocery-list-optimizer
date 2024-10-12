import React, { useEffect, useState } from 'react';
import axios from '../api/api';

function GroceryList() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        const fetchItems = async () => {
            const response = await axios.get('/items');
            setItems(response.data);
        };
        fetchItems();
    }, []);

    return (
        <div>
            <h2>Grocery List</h2>
            <ul>
                {items.map(item => (
                    <li key={item.id}>{item.name} (Quantity: {item.quantity})</li>
                ))}
            </ul>
        </div>
    );
}

export default GroceryList;
