import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { TextInput } from 'react-native-web';
import Touchable from './node_modules/react-native-web/src/exports/Touchable/index';
import MemoedTouchableOpacity from './node_modules/react-native-web/dist/exports/TouchableOpacity/index';
import Button from './node_modules/react-native-web/dist/exports/Button/index';
import setAndForwardRef from './node_modules/react-native-web/dist/vendor/react-native/Utilities/setAndForwardRef';
import AnimatedValueXY from './node_modules/react-native-web/dist/vendor/react-native/Animated/nodes/AnimatedValueXY';

export default function App() {
  return (
    <View style={styles.container}>     
      <Text styles={styles.titulo}>Calcule seu IMC</Text>
      <TextInput styles={styles.input} placeholder='Digite seu peso'></TextInput>
      <TextInput styles={styles.input} placeholder='Digite sua altura'></TextInput>
      <TouchableOpacity styles={styles.Button}>
        <text styles={styles.Button}>calculadora</text>
      </TouchableOpacity>
      <status style="auto"/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  titulo: {
    fontsize: 50,
    color:'#0ff',
    margintop: 50,
    textAlign: 'center'
    padding: 20,
    fontweight: 'bold',
  }
});
