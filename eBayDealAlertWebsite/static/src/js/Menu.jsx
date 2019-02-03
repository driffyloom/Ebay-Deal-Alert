import React from 'react';
import ReactDOM from 'react-dom';
//import Title from "./index.jsx";
//import Projects from "./project.jsx";
//import Contact from "./contact.jsx";

export default class Menu extends React.Component{
    constructor(props){
        super(props)
        //states any state (for things like clicked info inside etc. anything dynamic)
        this.state = {

        }
    }
    //initial stage that starts everything
    componentDidMount(){}

    //helper functions below

    //render for showing up on the page
    //put photo here
    render(){
        return(
            <div>
                <form action="{{ url_for('some_page') }}" method="GET">
                    <div class="form-group">
                        <label for="exampleInputEmail1">Search</label>
                        <input  class="form-control" name="searchBar" placeholder="Search Here!"></input>
                        <button type="submit" class="btn btn-primary"> Submit</button>
                    </div>
                </form>
            </div>
        )
    }
}

