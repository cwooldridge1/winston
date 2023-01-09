import React from 'react';
import { useSelector } from 'react-redux';
import { Chart, Code } from './content';
import { RootState } from '../redux';

const ContentManager = () => {
  const { content } = useSelector((state: RootState) => state.content);
  const types: { [key: string]: React.ComponentType } = {
    chart: Chart,
    code: Code,
  };
  return (
    <>
      {content.map((obj, i) => {
        const Component = types[obj.type];
        return <Component key={i} {...obj.props} />;
      })}
    </>
  );
};

export default ContentManager;
