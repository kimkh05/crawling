import { ThemeProvider } from "styled-components";
import { theme } from "./theme";
import { Global } from "./global";

export const StyleProvider = ({ children }) => {
  return (
    <ThemeProvider theme={theme}>
      <Global />
      {children}
    </ThemeProvider>
  );
};
