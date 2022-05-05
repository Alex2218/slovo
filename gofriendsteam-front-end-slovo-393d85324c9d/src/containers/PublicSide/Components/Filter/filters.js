import React, { useState, useEffect } from "react";
import { getFilter } from "../../../../actions/userActions";
import styles from './filter.module.css'
import find from '../../../../img/find.png'
// const host = "http://387d0007.ngrok.io";

const Filters = props => {
  const [filters, setFilters] = useState(null);
  useEffect(() => {
    getFilter().then(filters => setFilters(filters));
  }, []);

  const [selectedFilters, setSelectedFilters] = useState(null);

  const onChange = (event, key) => {
    setSelectedFilters({...selectedFilters, [key]: event.target.value})
  }

  const submit = () => {
    props.submit(selectedFilters)
  }

  console.log('filters', filters)

  return (
    <div className={styles.wrapper}>
      <select className={styles.select} onChange={(event) => onChange(event, 'tags')}>
        {filters && filters.tags.map(tag => (
          <option className={styles.option} key={tag.id} name={tag.id} value={tag.id}>{tag.tag}</option>
        ))}
      </select>
      <select className={styles.select} onChange={(event) => onChange(event, 'proffesions')}>
        {filters && filters.proffesions.map(tag => (
          <option className={styles.option} key={tag.id} name={tag.id} value={tag.id}>{tag.title}</option>
        ))}
      </select>
      <select className={styles.select} onChange={(event) => onChange(event, 'speakers')}>
        {filters && filters.speakers.map(tag => (
          <option className={styles.option} key={tag.id} name={tag.id} value={tag.id}>{tag.name}</option>
        ))}
      </select>
      <button className={styles.button} type='button' onClick={submit}><img className={styles.img} src={find}/></button>
    </div>
  );
};

export default Filters;
