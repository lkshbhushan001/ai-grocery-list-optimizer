import React from 'react';

const UserPreferences = ({ setUserName, fetchGroceryList }) => {
    const handleSubmit = (e) => {
        e.preventDefault();
        fetchGroceryList();
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                User Name:
                <input type="text" onChange={(e) => setUserName(e.target.value)} required />
            </label>
            <button type="submit">Get Grocery List</button>
        </form>
    );
};

export default UserPreferences;
