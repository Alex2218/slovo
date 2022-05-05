import React, { Component, Fragment, useEffect, useState } from "react";
import styles from "./accordion.module.css";


class Accordion extends React.Component {
    constructor(props) {
      super();
      let open = [];
      // console.log('props.children', props.children, props)
      props.children.forEach(item => {
        open.push(false);
      });
      this.state = {
        open: open
      };
    }
    
    isOpen(i) {
      return this.state.open[i];
    }
    
    toggle = (i) => {
      // console.log('Toggling ', i);
      return () => { 
        let newOpen = this.state.open;
        newOpen[i] = !newOpen[i];
        this.setState({
          open: newOpen
        });
      };
    }
    
    renderItems = () => {
      return React.Children.map(this.props.children, (item, i) => {
        if (i%2 === 0) {
          let open = this.state.open[i/2]
          return <div className={styles.title} onClick={this.toggle(Math.ceil(i/2))}>{open ? '− ' : '+ '}&nbsp;&nbsp;{item}</div>;
        } else {
          if (this.state.open[Math.floor(i/2)]) {
            return <div className={styles.content}>{item}</div>;
          }
        }
      });
    }
    
    render() {
      return (
        <div className={styles.accordion}>
          {this.renderItems()}
        </div>
      );
    }
  }

  export default Accordion;

  
//   class App extends React.Component {
//     render() {
//       return (
//         <main>
//         <Accordion>
//           One
//           <button>Content one</button>
//           Two
//           <span>Content two</span>
//           Three
//           <span>Content three</span>
//           Four
//           <span>Content four</span>
//         </Accordion>
//         </main>
//       );
//     }
//   }