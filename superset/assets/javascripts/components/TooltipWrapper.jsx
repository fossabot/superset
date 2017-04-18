import React from 'react';
import PropTypes from 'prop-types';
import { Tooltip, OverlayTrigger } from 'react-bootstrap';
import { slugify } from '../modules/utils';

const propTypes = {
  label: PropTypes.string.isRequired,
  tooltip: PropTypes.node,
  children: PropTypes.node.isRequired,
  placement: PropTypes.string,
};

const defaultProps = {
  placement: 'top',
};

export default function TooltipWrapper({ label, tooltip, children, placement }) {
  if (tooltip) {
    return (
      <OverlayTrigger
        placement={placement}
        overlay={<Tooltip id={`${slugify(label)}-tooltip`}>{tooltip}</Tooltip>}
      >
        {children}
      </OverlayTrigger>
    );
  }
  return children;
}

TooltipWrapper.propTypes = propTypes;
TooltipWrapper.defaultProps = defaultProps;
